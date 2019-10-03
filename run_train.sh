CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/ihdp_pnoise0.txt 7 &> logs/log_ihdp_pnoise0.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/ihdp_pnoise2.txt 7 &> logs/log_ihdp_pnoise2.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/ihdp_pnoise4.txt 7 &> logs/log_ihdp_pnoise4.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/ihdp_pnoise6.txt 7 &> logs/log_ihdp_pnoise6.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/ihdp_pnoise8.txt 7 &> logs/log_ihdp_pnoise8.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/ihdp_pnoise10.txt 7 &> logs/log_ihdp_pnoise10.txt &
