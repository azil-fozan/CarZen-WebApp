from BI import settings
from BI.constants import POSITIVE_WORDS, NEGATIVE_WORDS
from user_dashboards.models import Bill
from tempfile import NamedTemporaryFile
from asyncthreads import reactor
import boto3

from user_profiles.models import ServiceHistory


def get_receipt_product_data(receipt_id=0, data=None):
    if not data:
        data = Bill.objects.filter(receipt_id__id=receipt_id)

    response_data = []
    for row in data:
        temp_dict = {}
        temp_dict['id'] = row.id
        temp_dict['product_name'] = row.product_id.name
        temp_dict['unit'] = row.product_id.unit
        temp_dict['price'] = row.product_id.price
        temp_dict['discount'] = row.product_id.discount
        temp_dict['quantity'] = row.quantity
        temp_dict['total'] = round(
            (temp_dict['quantity'] * temp_dict['price']) * (1 - (temp_dict['discount'] / 100)), 2)
        response_data.append(temp_dict)
    return response_data


def download_file(bucket, key):
    s3 = boto3.client("s3", aws_access_key_id=settings.AWS_S3_ACCESS_KEY,
                          aws_secret_access_key=settings.AWS_S3_SECRET_KEY)
    s3_data = s3.get_object(Bucket= bucket, Key = key)
    contents = s3_data['Body'].read()  # your Excel's essence, pretty much a stream
    return contents


# yar sentiment analysis is deep learning, labled data chahiay isky liay.

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
# from tensorflow.keras.layers import Embedding
embedding_vector_length = 32

def define_and_train_for_SA():
    vocab_size = len(tokenizer.word_index) + 1
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_vector_length, input_length=200))
    model.add(SpatialDropout1D(0.25))
    model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
    print(model.summary())
    history = model.fit(padded_sequence,sentiment_label[0],validation_split=0.2, epochs=5, batch_size=32)

def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    print("Predicted label: ", sentiment_label[1][prediction])

# test_sentence1 = "I enjoyed my journey on this flight."
# predict_sentiment(test_sentence1)
# test_sentence2 = "This is the worst flight experience of my life!"
# predict_sentiment(test_sentence2)

def call_func_async(_func, **kwargs):
    r = reactor.Reactor()
    r.start()
    r.call_in_thread(_func, (kwargs))
    r.shutdown()

def get_sentiment_from_comment(service_id, user_role, comment):
    try:
        words = comment.split(' ')
        positivity = 0
        negativity = 0
        for word in words:
            if word.lower() in POSITIVE_WORDS:
                positivity += 1
            if word.lower() in NEGATIVE_WORDS:
                negativity += 1
        result = 'negative' if negativity > positivity else 'positive'
        if user_role == 1:
            ServiceHistory.objects.all(pk=service_id).update(sentiment=result)
        else:
            ServiceHistory.objects.all(pk=service_id).update(sentiment_owner=result)
    except:
        pass
