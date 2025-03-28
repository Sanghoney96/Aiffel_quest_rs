import tensorflow as tf


class BahdanauAttention(tf.keras.layers.Layer):
    def __init__(self, hidden_size):
        super(BahdanauAttention, self).__init__()
        self.w_dec = tf.keras.layers.Dense(hidden_size)
        self.w_enc = tf.keras.layers.Dense(hidden_size)
        self.w_com = tf.keras.layers.Dense(1)
    
    def call(self, h_enc, h_dec):
        h_enc = self.w_enc(h_enc)   # shape : (batch, length, hidden_size)
        h_dec = tf.expand_dims(h_dec, 1)    # shape : (batch, hidden_size) -> (batch, 1, hidden_size)
        h_dec = self.w_dec(h_dec)   

        score = self.w_com(tf.nn.tanh(h_dec + h_enc))
        
        attn = tf.nn.softmax(score, axis=1)

        context_vec = attn * h_enc
        context_vec = tf.reduce_sum(context_vec, axis=1)

        return context_vec, attn
    

class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, num_layers=1):
        super(Encoder, self).__init__()
        
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.Sequential([tf.keras.layers.GRU(enc_units,
                                                            return_sequences=True) 
                                        for _ in range(num_layers)])
        self.dropout = tf.keras.layers.Dropout(0.3)
        
    def call(self, x):
        out = self.embedding(x)
        out = self.gru(out)
        out = self.dropout(out)
        
        return out
    

class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, num_layers=1):
        super(Decoder, self).__init__()
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru_layers = [tf.keras.layers.GRU(dec_units,
                                               return_sequences=True, 
                                               return_state=True) 
                           for _ in range(num_layers)]
        self.dropout = tf.keras.layers.Dropout(0.3)
        self.fc = tf.keras.layers.Dense(vocab_size)
        self.attention = BahdanauAttention(self.dec_units)

    def call(self, x, h_dec, enc_out):
        out = self.embedding(x)
        
        # 모든 GRU 층을 처리
        for i, gru in enumerate(self.gru_layers):
            if i == len(self.gru_layers) - 1:  # 마지막 GRU 층에만 어텐션 적용
                context_vec, attn = self.attention(enc_out, h_dec)
                out = tf.concat([tf.expand_dims(context_vec, 1), out], axis=-1)
            out, h_dec = gru(out)
            out = self.dropout(out)
        
        out = self.fc(out)

        return out, h_dec, attn