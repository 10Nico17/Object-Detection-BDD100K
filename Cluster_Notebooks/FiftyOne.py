# Download BDD100K and convert to different formats


import fiftyone as fo
import fiftyone.zoo as foz

# The path to the source files that you manually downloaded
source_dir = "/home/krones2/Schreibtisch/bdd100k"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split="validation",
    source_dir=source_dir,
    copy_files=False,
)


#dataset_type = fo.types.COCODetectionDataset
#dataset_type = fo.types.YOLOv5Dataset

dataset_type = fo.types.CVATImageDataset




export_dir = "/home/krones2/Schreibtisch/Learning from Images Coding Project/CVAT_bdd100K/cvat"

# Export the dataset
dataset.export(
    export_dir=export_dir,
    dataset_type=dataset_type
    #export_media="copy",
    #label_field=label_field,
)

#session = fo.launch_app(dataset)
#session.wait()
