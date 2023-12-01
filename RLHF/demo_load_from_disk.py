# from datasets import load_dataset
# dataset = load_dataset("https://huggingface.co/datasets/beyond/rlhf-reward-single-round-trans_chinese", cache_dir="./dataset")
# dataset.save_to_disk('dataset/neulab/conala')



from datasets import Dataset, load_from_disk

# 创建一个简单的数据集
data = {
    "text": ["Hello", "How are you?", "Goodbye"],
    "label": [1, 0, 1]
}

simple_dataset = Dataset.from_dict(data)

# 保存数据集到磁盘
dataset_directory = 'RLHF/data/smaple'
simple_dataset.save_to_disk(dataset_directory)

# 从磁盘加载数据集
loaded_dataset = load_from_disk(dataset_directory)

# 打印加载的数据集
print(loaded_dataset)
