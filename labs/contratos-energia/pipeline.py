"""Núcleo de cálculo e tradução de texto separados da camada de arquivos."""
import argparse
import json
from pathlib import Path
import sys
from .energy import energy_si

def _no_constants(value):
    raise ValueError("Constante não permitida em JSON: "+value)

def _unique_keys(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError("Chave JSON duplicada: "+key)
        result[key]=value
    return result

def parse_request(text):
    if type(text) is not str:raise ValueError("Forneça texto JSON")
    data=json.loads(text,parse_constant=_no_constants,object_pairs_hook=_unique_keys)
    if type(data) is not dict or set(data)!={"unit_system","measurements"} or data["unit_system"]!="SI":
        raise ValueError("Objeto com unit_system=SI e measurements necessário")
    rows=data["measurements"]
    if type(rows) is not list or not rows or any(type(row) is not list or len(row)!=2 for row in rows):
        raise ValueError("measurements: lista não vazia de pares massa,velocidade")
    return tuple(tuple(row) for row in rows)

def energy_batch(rows):
    if type(rows) not in (list,tuple) or not rows or any(type(row) not in (list,tuple) or len(row)!=2 for row in rows):
        raise ValueError("Forneça lista ou tupla não vazia de pares")
    # A tupla de saída é nova; nenhum par de entrada é alterado.
    return tuple(energy_si(m,v) for m,v in rows)

def run_text(text):
    energies=energy_batch(parse_request(text))
    return json.dumps({"energy_unit":"J","energies":energies},allow_nan=False,sort_keys=True,indent=2)+"\n"

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path,help="JSON de entrada em SI")
    parser.add_argument("--output",type=Path,help="Novo arquivo JSON; nunca substitui existente")
    args=parser.parse_args(argv)
    try:
        # Valida e calcula tudo antes de abrir a saída.
        report=run_text(args.input.read_text(encoding="utf-8"))
        if args.output is None:
            sys.stdout.write(report)
        else:
            with args.output.open("x",encoding="utf-8") as stream:stream.write(report)
    except (OSError,UnicodeError,ValueError,ArithmeticError) as error:
        print("Erro: "+str(error),file=sys.stderr)
        return 2
    return 0

if __name__=="__main__":raise SystemExit(main())
