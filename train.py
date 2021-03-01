from models import get_model
from keras.preprocessing.image import ImageDataGenerator
import argparse


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    PARSER.add_argument('--arch_name', help='name of architecture',type=str)
    PARSER.add_argument('--folder', help='data folder',type=str)
    PARSER.add_argument('--save_model', help='save model name',type=str)
    PARSER.add_argument('--color_mode', help='color mode',type=str)
    PARSER.add_argument('--batch_size', help='batch size',type=int)
    PARSER.add_argument('--width', help='image width',type=int)
    PARSER.add_argument('--height', help='image height',type=int)
    PARSER.add_argument('--channels', help='image channels',type=int)
    PARSER.add_argument('--classes', help='no. of classes',type=int)
    PARSER.add_argument('--epochs', help='no. of epochs',type=int)

    ARGS = PARSER.parse_args()
    model = get_model(arch_name=ARGS.arch_name,input_shape=(ARGS.width,ARGS.height,ARGS.channels),\
        classes=ARGS.classes)
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    datagen = ImageDataGenerator(rescale=1./255)
    train_generator = datagen.flow_from_directory(ARGS.folder,  # this is the target directory
                                                target_size=(ARGS.height, ARGS.width),  # all images will be resized to 150x150
                                                batch_size=ARGS.batch_size,
                                                class_mode='categorical',
                                                color_mode=ARGS.color_mode)
    model.fit_generator(train_generator,
                   steps_per_epoch=len(train_generator)//ARGS.batch_size,
                   epochs=ARGS.epochs)

    model.save(ARGS.save_model)