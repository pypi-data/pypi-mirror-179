#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from palmiche.utils import tools
import os, glob
import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import multiprocessing as mp
import tempfile


def COM_dist_chunk_code(conf_file,grouplist,ndx,tpr,prefix):
    """
    This function doesn't have any relevance. It is only a code chunk 
    in order to parallelize the distance calculation. This must be outside of the function

    """
    tmp_row = [int(os.path.basename(conf_file).split(prefix)[-1].split('.')[0])]#Conf_ID, in this part is where the number is
    # HERE I NEED TO PUT THE TEMPORAL FILES

    opt_tmp = tempfile.NamedTemporaryFile(suffix='.opt')
    xvg_tmp = tempfile.NamedTemporaryFile(suffix='_dist.xvg') 
    with open(opt_tmp.name, 'w') as f:
        for (i, groups) in enumerate(grouplist):
            f.write(f"\"{i}\" com of group {groups[0]} plus com of group {groups[1]};\n")
    tools.run(f"gmx distance -s {tpr} -f {conf_file} -n {ndx} -sf {opt_tmp.name} -oall {xvg_tmp.name} -xvg none")
    tmp_row += list(np.loadtxt(xvg_tmp.name)[1:])
        
    Mean = stat.mean(tmp_row[1:])
    try:
        StDev = stat.stdev(tmp_row[1:])
    except:
        StDev = 0.0
    tmp_row += [Mean, StDev]
        
    for i in range(1,len(tmp_row)):
        tmp_row[i] = round(tmp_row[i],3)
    return tmp_row


def main(grouplist, cpu = 0, ndx = 'index.ndx', tpr = 'pull.tpr', xtc = 'pull.xtc', prefix = 'conf', out = 'summary_distances.dat', split_out_dir = '.'):
    """
    

    Parameters
    ----------
    grouplist : TYPE
        DESCRIPTION. A list of list,
        e.g.:
                ligands = ['LIA', 'LIB', 'LIC', 'LID', 'LIE']
                grouplist = [[ligand,ligand+"_CLOSE_AA"] for ligand in ligands]
                so...
                [(group1,group2), (group3,group4),...]
    cpu : TYPE, optional int
        DESCRIPTION. The default is 0. It will launch  as much as cpu has 
        the node the function COM_dist_chunk_code(). If some number is specified
        this will be the launched time of the function COM_dist_chunk_code().
    ndx : TYPE, optional
        DESCRIPTION. The default is 'index.ndx'.
    tpr : TYPE, optional
        DESCRIPTION. The default is 'pull.tpr'.
    xtc : TYPE, optional
        DESCRIPTION. The default is 'pull.xtc'.
    prefix : TYPE, optional
        DESCRIPTION. The default is 'conf'.
    out : TYPE, optional
        DESCRIPTION. The default is 'summary_distances.dat'.

    Returns
    -------
    None.

    """
    
    if not os.path.exists(ndx): 
        raise FileNotFoundError(f"\"{ndx}\" doesn't exist or is not accessible.")
    if not os.path.exists(tpr): 
        raise FileNotFoundError(f"\"{tpr}\" doesn't exist or is not accessible..")
    if not os.path.exists(xtc): 
        raise FileNotFoundError(f"\"{xtc}\" doesn't exist or is not accessible..")
    
    print('Splitting the trajectory...')
    tools.run(f"export GMX_MAXBACKUP=-1; echo 'system' | gmx trjconv -s {tpr} -f {xtc} -o {os.path.join(split_out_dir, prefix)}.gro -sep")
    print('Done!')
    conf_files = sorted(glob.glob(f"{os.path.join(split_out_dir, prefix)}[0-9]*"), key=lambda x:int(os.path.basename(x).split(prefix)[-1].split('.')[0]))
    
    columns = ["Conf_ID"] + [f"{item[0]}-{item[1]}" for item in grouplist] + ["Mean","StDev"]        
    data = []

    #In order to parallelize the dist calculation
    if cpu:
        jobs = cpu
    else:
        jobs = mp.cpu_count()
    pool = mp.Pool(jobs)
    
    data = pool.starmap(COM_dist_chunk_code, [(conf_file,grouplist,ndx,tpr,prefix) for conf_file in conf_files])
    
    pool.close()
    
    general_table = pd.DataFrame(data=data, columns = columns)
    general_table.plot(x="Conf_ID", y=columns[1:-1])
    plt.xlabel("Conf_ID")
    plt.ylabel("COM distance (nm)")
    plt.savefig('summary_distances.svg')
    #plt.show()
    
    
    with open(out, "w") as f:
        general_table.to_string(f,index=False)
    #general_table.to_csv(out, sep='\t', index=False)
    with open("mean.dat", "w") as f:
        general_table[["Conf_ID", "Mean"]].to_string(f,index=False, header=False)
    
    
if __name__=='__main__':
    grouplist = []
    for char in 'ABCDE':
        grouplist.append([f"LI{char}", f"LI{char}_CLOSE_AA"])
    path ="/home/ale/mnt/smaug/MD/NEW/docking_min_equi/umbrella_iteration/umbrella_N_ST/7e27/sys_MMV007839_Cell_891_SP_param"
    tools.makedirs('split_xtc')
    main(grouplist, cpu=6, ndx= os.path.join(path, 'index.ndx'), tpr=os.path.join(path,'pull.tpr'),
                    xtc=os.path.join(path, 'pull.xtc'), prefix='conf', out='summary_distances.dat', split_out_dir='split_xtc')
