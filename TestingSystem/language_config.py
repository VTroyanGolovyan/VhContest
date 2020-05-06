from runners import RunningSettings

# {0} - directory, {1} - path
languages = {
    'c++': RunningSettings(
        0,
        'g++ {1} -o {0}Main',
        'cd {0}; ./Main',
        '',
        'cpp'
    ),
    'python': RunningSettings(
        1,
        '',
        'python3 {1}',
        '',
        'py'
    ),
    'javascript': RunningSettings(
        1,
        '',
        'node {1}',
        '',
        'js'
    ),
    'php': RunningSettings(
        1,
        '',
        'php {1}',
        '',
        'php'
    ),
    'java': RunningSettings(
        2,
        'cd {0}; javac Main.java',
        'cd {0}; java Main',
        '',
        'java'
    )
}