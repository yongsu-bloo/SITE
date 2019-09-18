# CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/twins100.txt 1 > logs/log_twins100.txt
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/twins100_rand_0.1.txt 1 &> logs/log_twins100_rand_0.1.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/twins100_rand_0.2.txt 1 &> logs/log_twins100_rand_0.2.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/twins100_rand_0.3.txt 1 &> logs/log_twins100_rand_0.3.txt &
CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/twins100_rand_0.4.txt 1 &> logs/log_twins100_rand_0.4.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/twins100_rand_0.5.txt 1 &> logs/log_twins100_rand_0.5.txt &

CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/jobs_rand_0.1.txt 1 &> logs/log_jobs_rand_0.1.txt &
CUDA_VISIBLE_DEVICES="3" python site_param_search.py configs/jobs_rand_0.2.txt 1 &> logs/log_jobs_rand_0.2.txt &
CUDA_VISIBLE_DEVICES="0" python site_param_search.py configs/jobs_rand_0.3.txt 1 &> logs/log_jobs_rand_0.3.txt &
CUDA_VISIBLE_DEVICES="1" python site_param_search.py configs/jobs_rand_0.4.txt 1 &> logs/log_jobs_rand_0.4.txt &
CUDA_VISIBLE_DEVICES="2" python site_param_search.py configs/jobs_rand_0.5.txt 1 &> logs/log_jobs_rand_0.5.txt &
