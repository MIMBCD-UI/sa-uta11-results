<meta http-equiv="refresh" content="0; url='https://mimbcd-ui.github.io/sa-uta11-results/web/index.html'" />

# UTA11: Statistical Analysis Results

<img src="https://github.com/mida-project/meta/blob/master/banners/statistical-analysis.png?raw=true" width="100%" />

TODO

During this UTA11 study, we used several repositories to store the source code of our prototypes, later tested as *proof-of-concepts* under this research work. The prototypes are available in the [`prototype-assertive-proactive`](https://github.com/MIMBCD-UI/prototype-assertive-proactive), [`prototype-assertive-reactive`](https://github.com/MIMBCD-UI/prototype-assertive-reactive), [`prototype-non-assertive-proactive`](https://github.com/MIMBCD-UI/prototype-non-assertive-proactive), and [`prototype-non-assertive-reactive`](https://github.com/MIMBCD-UI/prototype-non-assertive-reactive) repositories. We deployed each prototype in a remote server. On the same hand, the hereby *results* represent the pieces of information of both [BreastScreening](https://BreastScreening.github.io) and [MIDA](https://mida-project.github.io) projects. These projects are research projects that deal with the use of a recently proposed technique in literature: [Deep Convolutional Neural Networks (CNNs)](https://en.wikipedia.org/wiki/Convolutional_neural_network). From a developed User Interface (UI) and *framework*, these deep networks will incorporate [several datasets](https://github.com/MIMBCD-UI/meta/wiki/Datasets) in different modes. You can find the [deployed prototypes](https://github.com/MIMBCD-UI/meta-private/blob/master/wiki/Technical.md#deployment-prototypes) on the [`Technical.md`](https://github.com/MIMBCD-UI/meta-private/blob/master/wiki/Technical.md#deployment-prototypes) file of the [`meta-private`](https://github.com/MIMBCD-UI/meta-private) repository. More information about the study is also available on the [`User-Research.md`](https://github.com/MIMBCD-UI/meta-private/blob/master/wiki/User-Research.md#test-11-assertive-and-non-assertive-introduction-) file of this [`meta-private`](https://github.com/MIMBCD-UI/meta-private) repository. Unfortunately, you need to be a member of our team to access the restricted information. We also have several demos to see in our [YouTube Channel](https://www.youtube.com/channel/UCPz4aTIVHekHXTxHTUOLmXw), please follow us.

## Citing

We kindly ask **scientific works and studies** that make use of the repository to cite it in their associated publications. Similarly, we ask **open-source** and **closed-source** works that make use of the repository to warn us about this use.

You can cite our work using the following BibTeX entry:

```
@inproceedings{10.1145/3544548.3580682,
author = {Calisto, Francisco Maria and Fernandes, Jo\~{a}o and Morais, Margarida and Santiago, Carlos and Abrantes, Jo\~{a}o Maria and Nunes, Nuno and Nascimento, Jacinto C.},
title = {Assertiveness-based Agent Communication for a Personalized Medicine on Medical Imaging Diagnosis},
year = {2023},
isbn = {9781450394215},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3399715.3399744},
doi = {10.1145/3544548.3580682},
abstract = {Intelligent agents are showing increasing promise for clinical decision-making in a variety of healthcare settings. While a substantial body of work has contributed to the best strategies to convey these agents’ decisions to clinicians, few have considered the impact of personalizing and customizing these communications on the clinicians’ performance and receptiveness. This raises the question of how intelligent agents should adapt their tone in accordance with their target audience. We designed two approaches to communicate the decisions of an intelligent agent for breast cancer diagnosis with different tones: a suggestive (non-assertive) tone and an imposing (assertive) one. We used an intelligent agent to inform about: (1) number of detected findings; (2) cancer severity on each breast and per medical imaging modality; (3) visual scale representing severity estimates; (4) the sensitivity and specificity of the agent; and (5) clinical arguments of the patient, such as pathological co-variables. Our results demonstrate that assertiveness plays an important role in how this communication is perceived and its benefits. We show that personalizing assertiveness according to the professional experience of each clinician can reduce medical errors and increase satisfaction, bringing a novel perspective to the design of adaptive communication between intelligent agents and clinicians.},
booktitle = {Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems},
articleno = {},
numpages = {20},
keywords = {Clinical Decision Support System, Healthcare, Breast Cancer},
location = {Hamburg, Germany},
series = {CHI '23}
}
```

## Table of contents

* [Prerequisites](#Prerequisites)
* [Usage](#Usage)
* [Roadmap](#Roadmap)
* [Contributing](#Contributing)
* [License & Copyright](#License--Copyright)
* [Team](#Team)
* [Acknowledgements](#Acknowledgements)

## Prerequisites

The following list is showing the required dependencies for this project to run locally:

* [Git](https://git-scm.com/) or any other Git or GitHub version control tool
* [Python](https://www.python.org/) (v3.5 or newer)
* [NodeJS](https://nodejs.org) (v16.14.1 or newer)

Here are some tutorials and documentation, if needed, to feel more comfortable about using and playing around with this repository:

* [Introduction to Node.js](https://nodejs.dev/en/learn)
* [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Git Tutorial](https://git-scm.com/docs/gittutorial)
* [GitHub Quick Tutorial](https://guides.github.com/activities/hello-world/)

## Usage

Usage follow the instructions here to setup the current repository and extract the present data. To understand how the hereby repository is used for, read the following steps.

### Installation

At this point, the only way to install this repository is manual. Eventually, this will be accessible through [pip](https://pypi.org/project/pip/) and [npm](https://www.npmjs.com/) or any other package managers, as mentioned on the [roadmap](#Roadmap).

Nonetheless, this kind of installation is as simple as cloning this repository. Virtually all Git and GitHub version control tools are capable of doing that. Through the console, we can use the command below, but other ways are also fine.

```bash
git clone https://github.com/MIMBCD-UI/sa-uta11-results.git
```

### Demonstration

Please, feel free to try out our demo. It is a script called `demo.py` at the `src/` directory. It can be used as follows:

```bash
python src/demo.py
```

Just keep in mind this is just a demo, so it does nothing more than downloading data to an arbitrary destination directory if the directory does not exist or does not have any content. Also, we did our best to make the demo as user-friendly as possible, so, above everything else, have fun! 😁

## Roadmap

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3819/badge)](https://bestpractices.coreinfrastructure.org/projects/3819)

We need to follow the repository goal, by addressing the thereby information. Therefore, it is of chief importance to scale this solution supported by the repository. The repository solution follows the best practices, achieving the [Core Infrastructure Initiative (CII)](https://bestpractices.coreinfrastructure.org/en/projects/3172) specifications.

Besides that, one of our goals involves creating a configuration file to automatically test and publish our code to pip or any other package manager. It will be most likely prepared for the [GitHub Actions](https://github.com/features/actions). Other goals may be written here in the future.

## Contributing

This project exists thanks to all the people who [contribute](CONTRIBUTING.md). We welcome everyone who wants to help us improve this downloader. As follows, we present some suggestions.

### Issuer

Either as something that seems missing or any need for support, just open a [new issue](https://github.com/MIMBCD-UI/sa-uta11-results/issues/new). Regardless of being a simple request or a fully-structured feature, we will do our best to understand them and, eventually, solve them.

### Developer

We like to develop, but we also like collaboration. You could ask us to add some features... Or you could want to do it yourself and fork this repository. Maybe even do some side-project of your own. If the latter ones, please let us share some insights about what we currently have.

## Information

The current information will summarize important items of this repository. In this section, we address all fundamental items that were crucial to the current information.

### Related Repositories

- [`sa-uta8-utaut`](https://github.com/mida-project/sa-uta8-utaut)

### Dataset Resources

To publish our [datasets](https://www.kaggle.com/MIMBCD-UI) we used a well known platform called [Kaggle](https://www.kaggle.com). To access our project's [Profile Page](https://www.kaggle.com/MIMBCD-UI) just follow the [link](https://www.kaggle.com/MIMBCD-UI). Here, you will find all of our published datasets and any associated information, such as descriptions and download links.

### License & Copyright

Copyright &copy; 2023 [Instituto Superior Técnico](http://tecnico.ulisboa.pt/)

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

The [`sa-uta11-results`](https://github.com/MIMBCD-UI/sa-uta11-results) repository is distributed under the terms of both [Academic License](https://github.com/MIMBCD-UI/prototype-breast-screening/blob/master/ACADEMIC.md) for academic purpose and [Commercial License](https://github.com/MIMBCD-UI/prototype-breast-screening/blob/master/COMMERCIAL.md) for commercial purpose, as well as under the [CC-BY-SA-4.0](COPYING.md) copyright. The content of the present repository has obtained the patent right of [World Intellectual Property Organization (WIPO)](https://www.wipo.int) invention. Moreover, the hereby invention for this repository is under protection of the patent number **[WO2022071818A1](https://patents.google.com/patent/WO2022071818A1)** with the application number **PCT/PT2021/050029**. The title of the invention is "*Computational Method and System for Improved Identification of Breast Lesions*", registered under the WO patent office.

See [ACADEMIC](https://github.com/MIMBCD-UI/prototype-breast-screening/blob/master/ACADEMIC.md) and [COMMERCIAL](https://github.com/MIMBCD-UI/prototype-breast-screening/blob/master/COMMERCIAL.md) for details. For more information about the [MIMBCD-UI](https://mimbcd-ui.github.io/) Project just follow the [link](https://github.com/MIMBCD-UI/meta).
