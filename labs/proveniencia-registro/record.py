"""Small provenance demonstration: hashes, safe replay of known local model, no network."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
try:
    from .model import solve
except ImportError:
    from model import solve

SOURCE_NAMES={'model.py','record.py'}
ARTIFACT_NAMES=SOURCE_NAMES|{'config.json','result.json'}
EXAMPLE={'rate_s_inv':'1','duration_s':'1','initial':'1','steps':4}


def encode(value):
    return (json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8')


def unique(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError('duplicate JSON key')
        result[key]=value
    return result


def nonfinite(value):
    raise ValueError('nonfinite JSON constant')


def decode(raw):
    if not isinstance(raw,bytes) or len(raw)>16384:raise ValueError('JSON bytes <=16KiB required')
    return json.loads(raw.decode('utf-8'),object_pairs_hook=unique,parse_constant=nonfinite)


def identity(raw):
    if not isinstance(raw,bytes):raise ValueError('bytes required')
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def known_sources():
    root=Path(__file__).parent
    return {name:(root/name).read_bytes() for name in SOURCE_NAMES}


def build(raw_config,sources,environment):
    config=decode(raw_config);value=solve(config)
    if not isinstance(sources,dict) or set(sources)!=SOURCE_NAMES or any(not isinstance(s,bytes) or len(s)>262144 for s in sources.values()):
        raise ValueError('two bounded source byte strings required')
    if not isinstance(environment,dict) or set(environment)!={'python','implementation','system'} or any(not isinstance(s,str) or len(s)>80 for s in environment.values()):
        raise ValueError('three short environment descriptions required')
    result={'endpoint':{'numerator':value.numerator,'denominator':value.denominator},'unit':'U'}
    bundle={**sources,'config.json':raw_config,'result.json':encode(result)}
    manifest=dict(protocol='provenance-demo-1',activity='explicit-euler-linear-decay',
                  model='dy/dt=-rate*y',units={'rate_s_inv':'s^-1','duration_s':'s','initial':'U','endpoint':'U'},
                  input_origin='synthetic prescribed parameters',randomness='none',
                  environment=environment,human_review='pending',
                  artifacts={name:identity(raw) for name,raw in sorted(bundle.items())})
    bundle['manifest.json']=encode(manifest)
    return bundle


def verify(bundle):
    """Byte consistency relative to the supplied unsigned manifest, not authenticity."""
    if not isinstance(bundle,dict) or set(bundle)!=ARTIFACT_NAMES|{'manifest.json'}:
        return ['artifact set differs']
    try:
        manifest=decode(bundle['manifest.json'])
        if not isinstance(manifest,dict) or manifest.get('protocol')!='provenance-demo-1' or set(manifest.get('artifacts',{}))!=ARTIFACT_NAMES:
            return ['manifest structure differs']
        return [name+' identity differs' for name in sorted(ARTIFACT_NAMES)
                if identity(bundle[name])!=manifest['artifacts'][name]]
    except (ValueError,TypeError,UnicodeError,KeyError):
        return ['manifest or artifact invalid']


def replay(bundle,expected_sources):
    issues=verify(bundle)
    if issues:return issues
    if not isinstance(expected_sources,dict) or set(expected_sources)!=SOURCE_NAMES:
        return ['known source set differs']
    if any(bundle[name]!=expected_sources[name] for name in SOURCE_NAMES):
        return ['source differs from known local implementation']
    try:
        if decode(bundle['manifest.json']).get('activity')!='explicit-euler-linear-decay':
            return ['unsupported activity']
        value=solve(decode(bundle['config.json']))
        expected={'endpoint':{'numerator':value.numerator,'denominator':value.denominator},'unit':'U'}
        return [] if decode(bundle['result.json'])==expected else ['result differs on known-model replay']
    except (ValueError,TypeError,KeyError,UnicodeError):return ['invalid model input or output']


def write_bundle(bundle,destination):
    if verify(bundle):raise ValueError('inconsistent bundle')
    destination=Path(destination)
    destination.mkdir() # Existing directory is rejected; no overwrite or cleanup of user files.
    for name,raw in bundle.items():
        with (destination/name).open('xb') as stream:stream.write(raw)


def main(argv=None):
    parser=argparse.ArgumentParser(description='Create a new synthetic provenance bundle; no network.',allow_abbrev=False)
    parser.add_argument('--output',type=Path,help='new directory, must not exist')
    args=parser.parse_args(argv)
    env=dict(python=platform.python_version(),implementation=platform.python_implementation(),system=platform.system())
    bundle=build(encode(EXAMPLE),known_sources(),env)
    if args.output:
        try:write_bundle(bundle,args.output)
        except (OSError,ValueError) as error:parser.error(str(error))
    print(bundle['manifest.json'].decode('utf-8'),end='')
    return 0

if __name__=='__main__':raise SystemExit(main())
