from keras.layers import Input
from keras.models import Model, load_model
from keras.optimizers import Adam
import os
import numpy as np


from . import metrics

#                   Adversarial Autoencoder
#   Paper: https://arxiv.org/pdf/1511.05644.pdf

#       Description:
#   Attach discriminator to autoencoder in oder to make decoder produce 
#   realistic samples from random noise and make encoder generate  more
#   useful latent representation of data. 

#       To do:
#   Find a way how to split sets into train and test ones
#   Get rid of modes because it does not really help
#   Insert mu, log, Lambda layers inside class

class AAE():
    def metric_test(self, set, pred_num = 32):    
        met_arr = np.zeros(pred_num)
        
        n_indx = np.random.choice(set.shape[0],pred_num)
        org_set = set[n_indx]
        
        noise = np.random.uniform(-1, 1, (pred_num, self.latent_dim))
        gen_set = self.encoder.predict([noise]) 
        met_arr = metrics.magic_distance(org_set, gen_set)
        return met_arr

    def __init__(self, input_shape, latent_dim = 100):
        self.input_shape = input_shape
        self.latent_dim = latent_dim
        
        self.build_discriminator = None
        self.build_encoder = None
        self.build_decoder = None
        
        self.best_model = None
        self.best_metric = 0
        
        self.epoch = 0
        self.history = None
     
    
    def build_models(self, optimizer = None, path = ''):
        if optimizer is None:
            optimizer = Adam(0.0002, 0.5)
    
        self.path = path
        if os.path.isfile(path+'/encoder.h5') and os.path.isfile(path+'/discriminator.h5'):
            self.encoder = load_model(path+'/encoder.h5')
            self.discriminator = load_model(path+'/discriminator.h5')
        else:
            if self.build_discriminator is None or self.build_encoder is None or self.build_decoder is None:
                raise Exception("Model building functions are not defined")
            else:
                # Build and compile the discriminator
                self.discriminator = self.build_discriminator()
                self.discriminator.compile(loss='binary_crossentropy', optimizer=optimizer)
                
                # Build the encoder
                self.encoder = self.build_encoder()
                self.decoder = self.build_decoder()

        # The encoder takes noise and the target label as input
        # and generates the corresponding digit of that label
        

        # For the combined model we will only train the encoder
        self.discriminator.trainable = False

        # The discriminator takes generated image as input and determines validity
        # and the label of that image
        
        
        input_img = Input(shape=self.input_shape)
        encod_img = self.encoder([input_img])
        
        decode = self.decoder(encod_img)
        valid = self.discriminator(encod_img)

        # The combined model  (stacked encoder and discriminator)
        # Trains encoder to fool discriminator
        
        self.combined = Model([input_img], [decode, valid])
        self.combined.compile(loss=['mse', 'binary_crossentropy'], loss_weights=[0.5, 0.5], optimizer=optimizer)
            
        print('models builded')    
            
    def save(self):
        self.encoder.save('encoder.h5')
        self.discriminator.save('discriminator.h5')
    
    def train(self, data_set, batch_size=32, epochs=1, verbose=True, checkpoint_range = 100, checkpoint_callback = None, validation_split = 0, save_best_model = False):
        """Trains the model for a given number of epochs (iterations on a dataset).
        # Arguments
            data_set: 
                Numpy array of training data.
            batch_size:
                Number of samples per gradient update.
            epochs: Number of epochs to train the model.
                An epoch is an iteration over batch sized samples of dataset.
            checkpoint_range:
                Range in witch checkpoint callback will be called and history data will be stored.
            verbose: 
                Integer. 0, 1. Verbosity mode.
            checkpoint_callback: List of `keras.callbacks.Callback` instances.
                Callback to apply during training on checkpoint stage.
            validation_split: Float between 0 and 1.
                Fraction of the training data to be used as validation data.
                The model will set apart this fraction of the training data,
                will not train on it, and will evaluate
                the loss and any model metrics
                on this data at the end of each epoch.
                The validation data is selected from the last samples.
            save_best_model:
                Boolean. If True, encoder weights will be resigned to best model according to chosen metric.
        # Returns
            A history object. 
        """ 
    
        '''
        if 0. < validation_split < 1.:
            split_at = int(data_set.shape[0] * (1. - validation_split))
            train_set = data_set[:split_at]
            valid_set = data_set[split_at:]
        else:
            train_set = data_set
            valid_set = None
    
        #collect statistical info of data
        data_set_std = np.std(data_set,axis = 0)
        data_set_mean = np.mean(data_set,axis = 0)
        '''
        # Adversarial ground truths
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        #mean min max
        max_hist_size = epochs//checkpoint_range + 1
        history = { 'gen_val'    :np.zeros((max_hist_size,3)), 
                    'train_val'  :np.zeros((max_hist_size,3)), 
                    'test_val'   :np.zeros((max_hist_size,3)), 
                    'control_val':np.zeros((max_hist_size,3)), 
                    'metric'     :np.zeros((max_hist_size,3)),
                    'best_metric':0,
                    'hist_size'  :0}
        
        for epoch in range(epochs):
            self.epoch = epoch
            
            # ---------------------
            #  Train Discriminator
            # ---------------------

            # Select a random batch of images
            idx = np.random.randint(0, data_set.shape[0], batch_size)
            imgs = data_set[idx]

            # Generate new latent representations
            gen_lats = self.encoder.predict([imgs])
            rnd_lats = np.random.uniform(-1, 1, (batch_size, self.latent_dim))
            #rnd_lats = np.random.normal(size=(batch_size, self.latent_dim))
            
            # Train the discriminator
            d_loss_real = self.discriminator.train_on_batch(rnd_lats, valid)
            d_loss_fake = self.discriminator.train_on_batch(gen_lats, fake)
            d_loss = (d_loss_real + d_loss_fake) / 2
            
            # ---------------------
            #  Train encoder
            # ---------------------
            
            # Train the encoder
            
            g_loss = self.combined.train_on_batch([imgs], [imgs, valid])[0]

            # Plot the progress
            if epoch % checkpoint_range == 0:
                gen_val = self.discriminator.predict([gen_lats])
                train_val = self.discriminator.predict([rnd_lats])
                
                '''
                if valid_set is not None: 
                    idx = np.random.randint(0, valid_set.shape[0], batch_size)
                    test_val = self.discriminator.predict(valid_set[idx])
                else:
                    test_val = np.zeros(batch_size)
                
                noise = np.random.normal(data_set_mean, data_set_std, (batch_size,)+ self.input_shape)
                cont_val = self.discriminator.predict(noise)
                 '''
                test_val = np.zeros(1)
                metric = np.zeros(1) #self.metric_test(train_set, 1000)
                if verbose:
                    print ("%d [D loss: %f] [G loss: %f] [validations TRN: %f, TST: %f] [metric: %f]" % (epoch, d_loss, g_loss, np.mean(train_val), np.mean(test_val), np.mean(metric)))
               
                hist_size = history['hist_size'] = history['hist_size']+1
                history['gen_val']    [hist_size-1] = np.mean(gen_val),  np.min(gen_val),  np.max(gen_val)
                history['train_val']  [hist_size-1] = np.mean(train_val),np.min(train_val),np.max(train_val)
                #history['test_val']   [hist_size-1] = np.mean(test_val), np.min(test_val), np.max(test_val)
                #history['control_val'][hist_size-1] = np.mean(cont_val), np.min(cont_val), np.max(cont_val) 
                #history['metric']     [hist_size-1] = np.mean(metric),   np.min(metric),   np.max(metric)
                
                if np.mean(metric)*0.98 < self.best_metric or self.best_model == None:
                    self.best_model = self.encoder.get_weights()
                    self.best_metric = np.mean(metric)
                    history['best_metric'] = self.best_metric
                    
                self.history = history
                
                if checkpoint_callback is not None:
                    checkpoint_callback()
        
        
        
        if save_best_model:
            self.encoder.set_weights(self.best_model)    
            
        self.epoch = epochs
        checkpoint_callback()   
        
        return self.history    