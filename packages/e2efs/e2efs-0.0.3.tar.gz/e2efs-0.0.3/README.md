# E2E-FS
E2E-FS: An End-to-End Feature Selection Method for Neural Networks

## CONTACT

This project is hosted at https://github.com/braisCB/E2E-FS. 

## REFERENCE

If you plan to use this code, please cite the following paper:

Cancela, B., Bolón-Canedo, V., & Alonso-Betanzos, A. (2020). 
E2E-FS: An End-to-End Feature Selection Method for Neural Networks. 
IEEE Transactions on Pattern Analysis and Machine Intelligence. *(Pending on publication)*

## EXAMPLE OF USE
    # REQUIRED IMPORTS TO CREATE THE MODEL
    from keras.datasets import mnist
    from keras.callbacks import LearningRateScheduler
    from keras.utils import to_categorical
    from keras import optimizers, models, layers
    # E2EFS IMPORT
    from e2efs import models


    # DEFINE YOUR CLASSIFIER
    def three_layer_nn(input_shape, nclasses):
        return models.Sequential([
            layers.Flatten(input_shape=input_shape),
            layers.Dense(50),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Dense(25),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Dense(10, activation='softmax')
        ])
    
    
    if __name__ == '__main__':
    
        ## LOAD DATA
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train = np.expand_dims(x_train, axis=-1)
        x_test = np.expand_dims(x_test, axis=-1)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
    
        ## LOAD MODEL AND COMPILE IT (NEVER FORGET TO COMPILE!)
        model = three_layer_nn(input_shape=x_train.shape[1:], nclasses=10)
        model.compile(optimizer=optimizers.SGD(), metrics=['acc'], loss='categorical_crossentropy')
    
        ## LOAD E2EFS AND RUN IT
        fs_class = models.E2EFSSoft(n_features_to_select=39).attach(model).fit(
            x_train, y_train, batch_size=128, validation_data=(x_test, y_test), verbose=2
        )
    
        ## FINE TUNING
        def scheduler(epoch):
            if epoch < 20:
                return .1
            elif epoch < 40:
                return .02
            elif epoch < 50:
                return .004
            else:
                return .0008
    
        fs_class.fine_tuning(x_train, y_train, epochs=60, batch_size=128, 
                             validation_data=(x_test, y_test),
                             callbacks=[LearningRateScheduler(scheduler)], verbose=2)
        print('FEATURE_RANKING :', fs_class.get_ranking())
        print('ACCURACY : ', fs_class.get_model().evaluate(x_test, y_test, batch_size=128)[-1])
        print('FEATURE_MASK NNZ :', np.count_nonzero(fs_class.get_mask()))
