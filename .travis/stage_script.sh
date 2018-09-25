# Screen must be 24bpp lest pyqt5 crashes, see pytest-dev/pytest-qt/35
XVFBARGS="-screen 0 1280x1024x24"

catchsegv xvfb-run -a -s "$XVFBARGS" pytest \
  --cov reinforcement/widgets/ reinforcement/widgets/tests/

if [[ "$TRAVIS_PULL_REQUEST" == "false" && "$TRAVIS_PYTHON_VERSION" == "3.6" ]]; then ./cc-test-reporter after-build -t coverage.py --exit-code $TRAVIS_TEST_RESULT; fi
