FROM registry.gitlab.com/empaia/integration/ci-docker-images/test-runner:0.1.40@sha256:c9b6f9e70ec8bf5ebe451b007e20bf41890ef6aef694a0afa45a4349674a2e90 AS build0

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY isyntax_backend /isyntax/isyntax_backend
COPY pyproject.toml /isyntax/pyproject.toml

WORKDIR /isyntax

RUN python3 -m venv .venv
RUN poetry build

FROM ubuntu:18.04@sha256:6fec50623d6d37b7f3c14c5b6fc36c73fd04aa8173d59d54dba00da0e7ac50ee

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install --no-install-recommends -y python3-pip python3-wheel unzip

COPY philips-pathologysdk-2.0-ubuntu18_04_py36_research.zip /isyntax/philips-pathologysdk-2.0-ubuntu18_04_py36_research.zip

WORKDIR /isyntax

RUN unzip philips-pathologysdk-2.0-ubuntu18_04_py36_research.zip \
    && cd philips-pathologysdk-2.0-ubuntu18_04_py36_research \
    && chmod 777 InstallPathologySDK.sh \
    && ./InstallPathologySDK.sh py3 -y \
    && cd .. \
    && rm -r philips-pathologysdk-2.0-ubuntu18_04_py36_research

COPY --from=build0 /isyntax/dist/*.whl /tmp
RUN pip3 install /tmp/*.whl

RUN mkdir /data

CMD ["python3", "-m", "isyntax_backend"]
