import os,yaml,logging,argparse

def read_params(config_path):
    with open(config_path) as f:
        config=yaml.safe_load(f)
    return config

def main(config_path,datasource_path):
    config=read_params(config_path)
    print(config)



if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default=os.path.join("config","params.yaml"))
    arg.add_argument("--datasource",default=None)

    parse_args=arg.parse_args()
    print(parse_args.config,parse_args.datasource)
    main(config_path=parse_args.config,datasource_path=parse_args.datasource)