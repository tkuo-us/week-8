# Week 8

This week's lab is meant to introduce you to Natural Language Processing (NLP), and provide a very brief survey of some methods used in the field. In particular, we'll cover the following:

- Preprocessing
- Vectorization
- Topic Modeling
- Visualization

*Note: in this course, will not cover the aspects of NLP which use artificial neural networks.*

## Setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: h501-week-8
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel
    - streamlit
    - seaborn
    - pandas
    - numpy
    - plotly
    - spacy
    - scikit-learn
    - corextopic
    - vaderSentiment
```

*Note: you are welcome to install more packages in your codespace, but they will not be used by the autograder.*
