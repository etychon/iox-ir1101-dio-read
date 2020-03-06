FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/alpine
COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
COPY requirements.txt /
RUN apk add --no-cache python py-pip
RUN pip install -r requirements.txt
COPY startup.py /
ENTRYPOINT python startup.py
