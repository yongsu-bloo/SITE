import sys
import os
import numpy as np
from subprocess import call
from tqdm import tqdm
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # shut up tensorflow

def load_config(cfg_file):
    cfg = {}

    with open(cfg_file,'r') as f:
        for l in f:
            l = l.strip()
            if len(l)>0 and not l[0] == '#':
                vs = l.split('=')
                if len(vs)>0:
                    k,v = (vs[0], eval(vs[1]))
                    if not isinstance(v,list):
                        v = [v]
                    cfg[k] = v
    return cfg

def sample_config(configs):
    cfg_sample = {}
    for k in configs.keys():
        opts = configs[k]
        c = np.random.choice(len(opts),1)[0]
        cfg_sample[k] = opts[c]
    return cfg_sample

def cfg_string(cfg):
    ks = sorted(cfg.keys())
    cfg_str = ','.join(['%s:%s' % (k, str(cfg[k])) for k in ks])
    return cfg_str.lower()

def is_used_cfg(cfg, used_cfg_file):
    cfg_str = cfg_string(cfg)
    used_cfgs = read_used_cfgs(used_cfg_file)
    return cfg_str in used_cfgs

def read_used_cfgs(used_cfg_file):
    used_cfgs = set()
    with open(used_cfg_file, 'r') as f:
        for l in f:
            used_cfgs.add(l.strip())

    return used_cfgs

def save_used_cfg(cfg, used_cfg_file):
    with open(used_cfg_file, 'a') as f:
        cfg_str = cfg_string(cfg)
        f.write('%s\n' % cfg_str)

def run(cfg_file, num_runs):
    configs = load_config(cfg_file)

    outdir = configs['outdir'][0]
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    used_cfg_file = '%s/used_configs.txt' % outdir


    ''' create results directory'''

    results_dir = configs['outdir'][0]
    results_parent_dir = results_dir.split('/')
    tmp_dir = '.'
    for k in results_parent_dir:
        tmp_dir  = tmp_dir + '/' + k
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
    print("============= Results are stored in %s ===========" %tmp_dir)

    if not os.path.isfile(used_cfg_file):
        f = open(used_cfg_file, 'w')
        f.close()

    for i in tqdm(range(num_runs)):
        cfg = sample_config(configs)
        if is_used_cfg(cfg, used_cfg_file):
            print 'Configuration used, skipping'
            continue
        save_used_cfg(cfg, used_cfg_file)

        ''' calculate the propensity '''
        propensity_dir = cfg['propensity_dir']
        if "normal" in cfg['datadir'] or "ber" in cfg['datadir']:
            listed_prop_dir = propensity_dir.split("/")
            prefix = cfg['datadir'].split("/")[-1]
            listed_prop_dir[-1] = prefix + listed_prop_dir[-1]
            propensity_dir = "/".join(listed_prop_dir)
        data_path = cfg['datadir'] + cfg['dataform']
        
        if not os.path.isfile(propensity_dir):
            call('python propensity_score_calculation.py %s %s' % (data_path, propensity_dir), shell=True)


        print '------------------------------'
        print 'Run %d of %d:' % (i+1, num_runs)
        print '------------------------------'
        print '\n'.join(['%s: %s' % (str(k), str(v)) for k,v in cfg.iteritems() if len(configs[k])>1])

        flags = ' '.join('--%s %s' % (k,str(v)) for k,v in cfg.iteritems())
        call('python site_net_train.py %s' % flags, shell=True)

        # Todo: insert overwrite and evaluate_period to flags
        # if 'evaluate_period' in configs and 'overwrite' in configs:
        #     if i % int(configs['evaluate_period'][0]) == 0:
        #         call('python evaluate.py %s %s' % (cfg_file, configs['overwrite']), shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Usage: python site_param_search.py <config file> <num runs>'
    else:
        run(sys.argv[1], int(sys.argv[2]))
