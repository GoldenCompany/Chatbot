FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6
RUN java -version
RUN python --version

RUN cd /usr/local/lib && \
    wget https://www.antlr.org/download/antlr-4.8-complete.jar && \
    export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH" && \
    alias antlr4='java -jar /usr/local/lib/antlr-4.8-complete.jar' && \
    alias grun='java org.antlr.v4.gui.TestRig'

COPY ./ /srv/project

WORKDIR /srv/project

RUN pip install antlr4-python3-runtime

ENTRYPOINT ["tail", "-f", "/dev/null"]
