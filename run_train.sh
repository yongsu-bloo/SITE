#! /bin/bash
CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/ihdp100-pnoise1.txt 20 &> logs/log_ihdp_pnoise1.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/ihdp100-pnoise2.txt 20 &> logs/log_ihdp_pnoise2.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/ihdp100-addnoise1.txt 20 &> logs/log_ihdp_addnoise1.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/ihdp100-addnoise2.txt 20 &> logs/log_ihdp_addnoise2.txt &
CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/jobs-pnoise1.txt 20 &> logs/log_jobs_pnoise1.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/jobs-pnoise2.txt 20 &> logs/log_jobs_pnoise2.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/jobs-addnoise1.txt 20 &> logs/log_jobs_addnoise1.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/jobs-addnoise2.txt 20 &> logs/log_jobs_addnoise2.txt &
CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/twins-pnoise1.txt 20 &> logs/log_twins_pnoise1.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/twins-pnoise2.txt 20 &> logs/log_twins_pnoise2.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/twins-addnoise1.txt 20 &> logs/log_twins_addnoise1.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/twins-addnoise2.txt 20 &> logs/log_twins_addnoise2.txt &
