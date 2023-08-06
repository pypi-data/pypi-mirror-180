FROM docker.io/fedora:latest

RUN dnf -y update

RUN dnf -y install python-devel python-build git-all

RUN yum -y install rsync

# install basic Python development and frequently used packages
RUN python3 -m pip install pytest numpy networkx matplotlib coverage

# entry point is bash shell
CMD ["/bin/bash"]