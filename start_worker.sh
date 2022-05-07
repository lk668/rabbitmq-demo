for i in {1..3}; do
    nohup python3 -u consumer.py > nohup"$i".log 2>&1 &
done