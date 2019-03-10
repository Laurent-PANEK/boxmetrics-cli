from boxmetrics.main import BoxmetricsTest


def test_boxmetrics(tmp):
    with BoxmetricsTest() as app:
        res = app.run()
        print(res)
        raise Exception


def test_command1(tmp):
    argv = ["command1"]
    with BoxmetricsTest(argv=argv) as app:
        app.run()
