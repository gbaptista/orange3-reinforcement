
for script in \
    install_orange3_reinforcement.sh \
    install_pyqt.sh \
    install_openai_baselines.sh
do
    foldable source $TRAVIS_BUILD_DIR/.travis/$script
done
