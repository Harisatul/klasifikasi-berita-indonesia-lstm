from pprint import pprint
from NaiveBayesClassifier import NaiveBayesClassifier

if __name__ == '__main__':
    text = """
`   Halo Bulan terbentuk pada saat cahaya dibiaskan, lalu dipantulkan dan disebarkan atau dibiaskan melalui kristal es yang tertahan di awan cirrus atau cirrostratus yang berada di ketinggian 6.000 meter, bahkan lebih tinggi hingga 12.000 meter. Selanjutnya bentuk kristal es ini akan memfokuskan cahaya menjadi lingkaran cahaya di sekitar bulan atau matahari, kalau pada mataharo disebut fenomena halo Matahari.
    """
    classifier = NaiveBayesClassifier()
    result = classifier.classifier(text)
    pprint(result)