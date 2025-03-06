import tensorflow as tf

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, 
                                                            reduction='none')

def loss_function(y_true, y_pred):
    mask = tf.math.not_equal(y_true, 0)
    loss = loss_object(y_true, y_pred)
    
    mask = tf.cast(mask, dtype=loss.dtype)
    loss *= mask
    
    return tf.reduce_mean(loss)