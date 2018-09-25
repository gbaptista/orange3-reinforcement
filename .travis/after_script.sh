if [[ "$TRAVIS_PULL_REQUEST" == "false" && "$TRAVIS_PYTHON_VERSION" == "3.6" ]]
then
  coverage xml
  ./cc-test-reporter after-build -t coverage.py --exit-code $TRAVIS_TEST_RESULT
fi
