import os,yaml,logging,argparse



if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="default")
    arg.add_argument("--datasource",default=None)

    parse_args=arg.parse_args()
    print(parse_args.config,parse_args.datasource)