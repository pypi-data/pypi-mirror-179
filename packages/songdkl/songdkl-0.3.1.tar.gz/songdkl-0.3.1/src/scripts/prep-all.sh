# shell script to prepare all data
# this script assumes you have already run ./scripts/download_pcb_dataset.py
songdkl prep data/pcb_data/song_data/*/ \
  --output_dir_path ./results/pcb_data/song_data | tee ./results/pcb_data/song_data/prep-all-log.txt
