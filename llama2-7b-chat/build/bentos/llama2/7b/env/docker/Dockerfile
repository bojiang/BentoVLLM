# ===========================================
#
# THIS IS A GENERATED DOCKERFILE. DO NOT EDIT
#
# ===========================================

# Block SETUP_BENTO_BASE_IMAGE
FROM yatai/pytorch:3.11-2.1.2-1.2.9 as base-container

ENV LANG=C.UTF-8

ENV LC_ALL=C.UTF-8

ENV PYTHONIOENCODING=UTF-8

ENV PYTHONUNBUFFERED=1



# Block SETUP_BENTO_USER
ARG BENTO_USER=bentoml
ARG BENTO_USER_UID=1034
ARG BENTO_USER_GID=1034
RUN groupadd -g $BENTO_USER_GID -o $BENTO_USER && useradd -m -u $BENTO_USER_UID -g $BENTO_USER_GID -o -r $BENTO_USER
ARG HF_TOKEN=
ENV HF_TOKEN=$HF_TOKEN
ARG BENTO_PATH=/home/bentoml/bento
ENV BENTO_PATH=$BENTO_PATH
ENV BENTOML_HOME=/home/bentoml/

RUN mkdir $BENTO_PATH && chown bentoml:bentoml $BENTO_PATH -R
WORKDIR $BENTO_PATH


# Block SETUP_BENTO_COMPONENTS
COPY --chown=bentoml:bentoml ./env/python ./env/python/
# install python packages with install.sh
RUN bash -euxo pipefail /home/bentoml/bento/env/python/install.sh
COPY --chown=bentoml:bentoml . ./

# Block SETUP_BENTO_ENTRYPOINT
# Default port for BentoServer
EXPOSE 3000

# Expose Prometheus port
EXPOSE 3001

RUN chmod +x /home/bentoml/bento/env/docker/entrypoint.sh

USER bentoml

ENTRYPOINT [ "/home/bentoml/bento/env/docker/entrypoint.sh" ]

