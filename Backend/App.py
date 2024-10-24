from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

services = [
           {
            "CreatedAt": "2024-10-22T11:39:14.527898728Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 5009,
                        "TargetPort": 5000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.34/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    }
                ]
            },
            "ID": "2gw5ib9uadw1g3pj9hrcvossl",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "registry",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "registry:2@sha256:ac0192b549007e22998eb74e8d8488dcfe70f1489520c3b144a6047ac5efbe90",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T11:39:14.529226176Z",
            "Version": {
                "Index": 907
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.115712028Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8000,
                        "TargetPort": 8000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.39/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.3.4/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "3p2or3dy92bs581vvy4g98u2r",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "Labels": {
                    "com.docker.stack.image": "127.0.0.1:5009/stackdemo",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "127.0.0.1:5009/stackdemo:latest@sha256:603d9870a2106a1df59d0facb21035f0dab172ce002bca6a315759ab73f99f3e",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "web"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.116889721Z",
            "Version": {
                "Index": 972
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.092274858Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.2/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "7yh9o64pwfajm1wfzkt1btq41",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "nginx:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "nginx"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.093541313Z",
            "Version": {
                "Index": 968
            }
        },
        {
            "CreatedAt": "2024-10-22T06:03:09.217912722Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8080,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.16/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.2/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "jvd4az2zt7mhye83bdxc1fbfe",
            "PreviousSpec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 3
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T06:29:44.702176129Z",
            "Version": {
                "Index": 157
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:03.477045805Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.8/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "tcvy8fk3zpw5b14lnblm7pt2q",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "redis:alpine",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_redis",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "redis:alpine@sha256:de13e74e14b98eb96bdf886791ae47686c3c5d29f9d5f85ea55206843e3fce26",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "redis"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:03.478516452Z",
            "Version": {
                "Index": 982
            }
        },
        {
            "CreatedAt": "2024-10-22T07:15:37.379890184Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 80,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.25/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.98/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "ud0e8ijpowu0flf32xvwc8ssc",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T07:15:37.381195741Z",
            "Version": {
                "Index": 769
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:05.841535137Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.10/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "updbxooeiwhlvpnva0va7oiaq",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "alpine:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_alpine",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "alpine:latest@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        },
                        "TTY": True
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "alpine"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:05.844163736Z",
            "Version": {
                "Index": 992
            }
        },
        {
            "CreatedAt": "2024-10-22T11:39:14.527898728Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 5009,
                        "TargetPort": 5000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.34/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    }
                ]
            },
            "ID": "2gw5ib9uadw1g3pj9hrcvossl",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "registry",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "registry:2@sha256:ac0192b549007e22998eb74e8d8488dcfe70f1489520c3b144a6047ac5efbe90",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T11:39:14.529226176Z",
            "Version": {
                "Index": 907
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.115712028Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8000,
                        "TargetPort": 8000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.39/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.3.4/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "3p2or3dy92bs581vvy4g98u2r",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "Labels": {
                    "com.docker.stack.image": "127.0.0.1:5009/stackdemo",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "127.0.0.1:5009/stackdemo:latest@sha256:603d9870a2106a1df59d0facb21035f0dab172ce002bca6a315759ab73f99f3e",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "web"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.116889721Z",
            "Version": {
                "Index": 972
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.092274858Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.2/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "7yh9o64pwfajm1wfzkt1btq41",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "nginx:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "nginx"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.093541313Z",
            "Version": {
                "Index": 968
            }
        },
        {
            "CreatedAt": "2024-10-22T06:03:09.217912722Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8080,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.16/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.2/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "jvd4az2zt7mhye83bdxc1fbfe",
            "PreviousSpec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 3
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T06:29:44.702176129Z",
            "Version": {
                "Index": 157
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:03.477045805Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.8/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "tcvy8fk3zpw5b14lnblm7pt2q",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "redis:alpine",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_redis",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "redis:alpine@sha256:de13e74e14b98eb96bdf886791ae47686c3c5d29f9d5f85ea55206843e3fce26",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "redis"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:03.478516452Z",
            "Version": {
                "Index": 982
            }
        },
        {
            "CreatedAt": "2024-10-22T07:15:37.379890184Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 80,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.25/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.98/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "ud0e8ijpowu0flf32xvwc8ssc",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T07:15:37.381195741Z",
            "Version": {
                "Index": 769
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:05.841535137Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.10/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "updbxooeiwhlvpnva0va7oiaq",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "alpine:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_alpine",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "alpine:latest@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        },
                        "TTY": True
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "alpine"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:05.844163736Z",
            "Version": {
                "Index": 992
            }
        },
        {
            "CreatedAt": "2024-10-22T11:39:14.527898728Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 5009,
                        "TargetPort": 5000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.34/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    }
                ]
            },
            "ID": "2gw5ib9uadw1g3pj9hrcvossl",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 5009,
                            "TargetPort": 5000
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "registry",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "registry:2@sha256:ac0192b549007e22998eb74e8d8488dcfe70f1489520c3b144a6047ac5efbe90",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T11:39:14.529226176Z",
            "Version": {
                "Index": 907
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.115712028Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8000,
                        "TargetPort": 8000
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.39/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.3.4/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "3p2or3dy92bs581vvy4g98u2r",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8000,
                            "TargetPort": 8000
                        }
                    ]
                },
                "Labels": {
                    "com.docker.stack.image": "127.0.0.1:5009/stackdemo",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "127.0.0.1:5009/stackdemo:latest@sha256:603d9870a2106a1df59d0facb21035f0dab172ce002bca6a315759ab73f99f3e",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "web"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.116889721Z",
            "Version": {
                "Index": 972
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:01.092274858Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.2/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "7yh9o64pwfajm1wfzkt1btq41",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "nginx:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "nginx"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:01.093541313Z",
            "Version": {
                "Index": 968
            }
        },
        {
            "CreatedAt": "2024-10-22T06:03:09.217912722Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 8080,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.16/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.2/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "jvd4az2zt7mhye83bdxc1fbfe",
            "PreviousSpec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 8080,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 3
                    }
                },
                "Name": "my-nginx",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T06:29:44.702176129Z",
            "Version": {
                "Index": 157
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:03.477045805Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.8/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "tcvy8fk3zpw5b14lnblm7pt2q",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "redis:alpine",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_redis",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "redis:alpine@sha256:de13e74e14b98eb96bdf886791ae47686c3c5d29f9d5f85ea55206843e3fce26",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        }
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "redis"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:03.478516452Z",
            "Version": {
                "Index": 982
            }
        },
        {
            "CreatedAt": "2024-10-22T07:15:37.379890184Z",
            "Endpoint": {
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "PublishMode": "ingress",
                        "PublishedPort": 80,
                        "TargetPort": 80
                    }
                ],
                "Spec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.0.25/24",
                        "NetworkID": "lt58xre1i7zb1r4vvuwia72mv"
                    },
                    {
                        "Addr": "10.0.2.98/24",
                        "NetworkID": "kr5au1x7ypspdyz21oo7o6x7x"
                    }
                ]
            },
            "ID": "ud0e8ijpowu0flf32xvwc8ssc",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip",
                    "Ports": [
                        {
                            "Protocol": "tcp",
                            "PublishMode": "ingress",
                            "PublishedPort": 80,
                            "TargetPort": 80
                        }
                    ]
                },
                "Labels": {},
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "web",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "DNSConfig": {},
                        "Image": "nginx:latest@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb",
                        "Init": False,
                        "Isolation": "default"
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Target": "kr5au1x7ypspdyz21oo7o6x7x"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "mips64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "unknown",
                                "OS": "unknown"
                            }
                        ]
                    },
                    "Resources": {
                        "Limits": {},
                        "Reservations": {}
                    },
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T07:15:37.381195741Z",
            "Version": {
                "Index": 769
            }
        },
        {
            "CreatedAt": "2024-10-22T12:40:05.841535137Z",
            "Endpoint": {
                "Spec": {
                    "Mode": "vip"
                },
                "VirtualIPs": [
                    {
                        "Addr": "10.0.3.10/24",
                        "NetworkID": "a33gruskditrg5kffyno08n77"
                    }
                ]
            },
            "ID": "updbxooeiwhlvpnva0va7oiaq",
            "Spec": {
                "EndpointSpec": {
                    "Mode": "vip"
                },
                "Labels": {
                    "com.docker.stack.image": "alpine:latest",
                    "com.docker.stack.namespace": "c"
                },
                "Mode": {
                    "Replicated": {
                        "Replicas": 1
                    }
                },
                "Name": "c_alpine",
                "TaskTemplate": {
                    "ContainerSpec": {
                        "Image": "alpine:latest@sha256:beefdbd8a1da6d2915566fde36db9db0b524eb737fc57cd1367effd16dc0d06d",
                        "Isolation": "default",
                        "Labels": {
                            "com.docker.stack.namespace": "c"
                        },
                        "Privileges": {
                            "CredentialSpec": None,
                            "NoNewPrivileges": False,
                            "SELinuxContext": None
                        },
                        "TTY": True
                    },
                    "ForceUpdate": 0,
                    "Networks": [
                        {
                            "Aliases": [
                                "alpine"
                            ],
                            "Target": "a33gruskditrg5kffyno08n77"
                        }
                    ],
                    "Placement": {
                        "Platforms": [
                            {
                                "Architecture": "amd64",
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "OS": "linux"
                            },
                            {
                                "Architecture": "arm64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "386",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "ppc64le",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "riscv64",
                                "OS": "linux"
                            },
                            {
                                "Architecture": "s390x",
                                "OS": "linux"
                            }
                        ]
                    },
                    "Resources": {},
                    "Runtime": "container"
                }
            },
            "UpdatedAt": "2024-10-22T12:40:05.844163736Z",
            "Version": {
                "Index": 992
            }
        }
    ]


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "hello"})

@app.route('/services/<service_id>', methods=['GET'])
def get_service(service_id):
    service = next((s for s in services if s['id'] == service_id), None)
    if service:
        print("GET")
        return jsonify(service)
    else:
        return jsonify({'error': 'Service not found'}), 404

@app.route('/services', methods=['GET'])
def all_services():
    return jsonify(services)

@app.route('/services/<service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = next((s for s in services if s['id'] == service_id), None)
    services.remove(service)
    print(service)
    return services