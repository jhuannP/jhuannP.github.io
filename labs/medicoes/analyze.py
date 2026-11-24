"""Laboratório original: medições sintéticas e ajuste linear não ponderado."""
from dataclasses import dataclass
from math import isfinite, fsum, sqrt
from pathlib import Path
import argparse
import csv
import hashlib
import io
import json
import platform
import sys

@dataclass(frozen=True)
class Measurement:
    time_s: float
    position_m: float

    def __post_init__(self):
        for value in (self.time_s,self.position_m):
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not isfinite(value):
                raise ValueError('Medições precisam de números reais finitos')
        if self.time_s<0:raise ValueError('Tempo deve ser não negativo')


def validate_samples(samples):
    rows=tuple(samples)
    if len(rows)<2:raise ValueError('São necessárias pelo menos duas medições')
    if any(not isinstance(row,Measurement) for row in rows):raise ValueError('Use objetos Measurement')
    if any(b.time_s<=a.time_s for a,b in zip(rows,rows[1:])):
        raise ValueError('Tempos devem estar em ordem estritamente crescente, sem duplicatas')
    return rows


def parse_csv(text):
    if not isinstance(text,str):raise ValueError('CSV deve ser fornecido como texto')
    reader=csv.DictReader(io.StringIO(text.lstrip('\ufeff')),strict=True)
    samples=[]
    try:
        # fieldnames também lê o cabeçalho e pode lançar csv.Error.
        if reader.fieldnames!=['time_s','position_m']:
            raise ValueError('Cabeçalho esperado: time_s,position_m')
        for row in reader:
            if None in row or any(v is None or not v.strip() for v in row.values()):
                raise ValueError(f'Linha {reader.line_num}: campo ausente ou coluna extra')
            try:samples.append(Measurement(float(row['time_s']),float(row['position_m'])))
            except (ValueError,OverflowError) as error:
                raise ValueError(f'Linha {reader.line_num}: {error}') from error
    except csv.Error as error:raise ValueError(f'CSV inválido: {error}') from error
    return validate_samples(samples)


def fit_line(samples):
    rows=validate_samples(samples);n=len(rows)
    try:
        mt=fsum(row.time_s/n for row in rows)
        mx=fsum(row.position_m/n for row in rows)
        stt=fsum((row.time_s-mt)**2 for row in rows)
        stx=fsum((row.time_s-mt)*(row.position_m-mx) for row in rows)
        if stt<=0 or not isfinite(stt):raise ValueError('Escala de tempo inadequada ao ajuste')
        velocity=stx/stt;intercept=mx-velocity*mt
        residuals=[row.position_m-(intercept+velocity*row.time_s) for row in rows]
        SSE=fsum(r*r for r in residuals)
        result=dict(count=n,intercept_m=intercept,velocity_m_s=velocity,
                    SSE_m2=SSE,RMSE_m=sqrt(SSE/n),residuals_m=residuals)
        values=[intercept,velocity,SSE,result['RMSE_m'],*residuals]
        if not all(isfinite(v) for v in values):raise ValueError('Resultado não finito; reveja escala dos dados')
        return result
    except OverflowError as error:
        raise ValueError('Escala numérica excessiva para este método didático') from error


def make_report(samples,raw_bytes,name,source_kind='unspecified'):
    if source_kind not in ('synthetic','unspecified'):raise ValueError('Origem deve ser explicitada')
    return dict(schema_version=1,experiment='linear-position-fit',
                config={'method':'OLS com intercepto','weights':'iguais','units':{'time':'s','position':'m'}},
                input={'name':Path(name).name,'sha256':hashlib.sha256(raw_bytes).hexdigest(),
                       'source_kind':source_kind},
                software={'python':platform.python_version(),'implementation':platform.python_implementation(),
                          'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                result=fit_line(samples),
                interpretation='Resumo de ajuste; não valida movimento real, erro de medição ou mecanismo científico.')


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True,help='CSV com time_s,position_m')
    parser.add_argument('--output',type=Path,help='Novo arquivo JSON; não substitui arquivo existente')
    parser.add_argument('--source-kind',choices=('synthetic','unspecified'),default='unspecified')
    args=parser.parse_args(argv)
    try:
        raw=args.input.read_bytes()
        rows=parse_csv(raw.decode('utf-8-sig'))
        report=make_report(rows,raw,args.input.name,args.source_kind)
        text=json.dumps(report,ensure_ascii=False,allow_nan=False,indent=2)+'\n'
        if args.output:
            with args.output.open('x',encoding='utf-8') as stream:stream.write(text)
        else:print(text,end='')
    except (OSError,UnicodeError,ValueError) as error:
        print(f'Erro: {error}',file=sys.stderr)
        return 2
    return 0

if __name__=='__main__':raise SystemExit(main())
