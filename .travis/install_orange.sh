foldable pip install -U setuptools pip codecov

cat requirements-dev.txt \
    requirements.txt |
    while read dep; do
        dep="${dep%%#*}"  # Strip the comment
        [ "$dep" ] &&
            foldable pip install $dep
    done

cd $TRAVIS_BUILD_DIR
