import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers.experimental import preprocessing as tfp

from config import Config



def build_dataset(cfg):
    dataset_train = tf.keras.preprocessing.image_dataset_from_directory(
        cfg.datapath,
        validation_split=cfg.validation_split,
        subset="training",
        seed=cfg.seed,
        image_size=(cfg.img_size, cfg.img_size),
        batch_size=cfg.batch_size,
    )

    dataset_train = dataset_train.prefetch(tf.data.AUTOTUNE)
    dataset_val = tf.keras.preprocessing.image_dataset_from_directory(
        cfg.datapath,
        validation_split=cfg.validation_split,
        subset="validation",
        seed=cfg.seed,
        image_size=(cfg.img_size, cfg.img_size),
        batch_size=cfg.batch_size,
    )
    dataset_val = dataset_val.prefetch(tf.data.AUTOTUNE)

    # Data augmentation
    data_augmentation = tf.keras.Sequential(
        [
            tfp.Rescaling(1.0 / 255),
            tfp.RandomFlip("horizontal"),
            tfp.RandomFlip("vertical"),
            tfp.RandomRotation(0.2),
            tfp.RandomZoom(0.2),
        ]
    )

    dataset_train = dataset_train.map(lambda x, y: (data_augmentation(x, training=True), y))

    return dataset_train, dataset_val

if __name__ == '__main__':
    cfg = Config()
    dataset_train, dataset_val = build_dataset(cfg)
    url = "https://tfhub.dev/google/imagenet/mobilenet_v3_large_100_224/classification/5"
    embed = hub.KerasLayer(url, input_shape=(cfg.img_size, cfg.img_size, 3))
    model = tf.keras.Sequential([embed, 
                                 tf.keras.layers.Dense(cfg.num_classes, activation='softmax')])
    print(model.summary())

    model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'])
    model.fit(dataset_train, epochs=10, validation_data=dataset_val)

    model.save('mobilenetv3_large_100_224', save_format='tf')

