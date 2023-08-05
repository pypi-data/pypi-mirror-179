from jsonpath import jsonpath
import json


def envpathToEnvinfo(env_all_path):
    try:
        env_info = list(map(lambda x: x.strip(), env_all_path.split(',')))
        if len(env_info) == 3:
            env_path = env_info[0]
            with open(env_path, 'r', encoding='utf-8')as f:
                envs = json.loads(f.read())
            env = jsonpath(envs, f'$..[?(@.{env_info[1]}=="{env_info[2]}")]')[0]
            return env
    except Exception:
        return dict()