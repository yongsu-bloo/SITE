python evaluate.py configs/ihdp.txt 1 &> logs/eval_ihdp
python evaluate.py configs/noisy_25_ihdp.txt 1 &> logs/eval_noisy_25_ihdp
python evaluate.py configs/noisy_100_ihdp.txt 1 &> logs/eval_noisy_100_ihdp
python evaluate.py configs/noisy_200_ihdp.txt 1 &> logs/eval_noisy_200_ihdp
python evaluate.py configs/noisy_1000_ihdp.txt 1 &> logs/eval_noisy_1000_ihdp

python evaluate.py configs/jobs.txt 1 &> logs/eval_jobs
python evaluate.py configs/noisy_17_jobs.txt 1 &> logs/eval_noisy_17_jobs
python evaluate.py configs/noisy_100_jobs.txt 1 &> logs/eval_noisy_100_jobs
python evaluate.py configs/noisy_200_jobs.txt 1 &> logs/eval_noisy_200_jobs
python evaluate.py configs/noisy_1000_jobs.txt 1 &> logs/eval_noisy_1000_jobs

python evaluate.py configs/twins.txt 1 &> logs/eval_twins
python evaluate.py configs/noisy_40_twins.txt 1 &> logs/eval_noisy_40_twins
python evaluate.py configs/noisy_100_twins.txt 1 &> logs/eval_noisy_100_twins
python evaluate.py configs/noisy_200_twins.txt 1 &> logs/eval_noisy_200_twins
python evaluate.py configs/noisy_1000_twins.txt 1 &> logs/eval_noisy_1000_twins
