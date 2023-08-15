import confutilPPP


def test():
    CONFIG = {
        'test': 'test'
    }
    conf = confutilPPP.check_config(_object=CONFIG, _filename='config')
    print(conf)


if __name__ == '__main__':
    test()
