FROM golang

COPY ./i.go /root/i.go
CMD go run /root/i.go -t 12000