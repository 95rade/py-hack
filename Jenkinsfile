// This shows a simple build wrapper example, using the Timestamper plugin.
node {
    echo "NODE_NAME = ${env.NODE_NAME}"
    //TODO: figure out how to 'delete workspace before each build'
    // Adds timestamps to the output logged by steps inside the wrapper.
    timestamps {
        // Just some echoes to show the timestamps.
        stage "Clone repo"
            echo "Hey, look, I'm echoing with a timestamp!"
            echo '${WORKSPACE}'
            sh 'rm -rf py-hack'
            sh 'git clone https://github.com/95rade/py-hack.git'
            //sh 'cd py-hack'
            sh 'ls -al'
            sh 'pwd'
            sh 'cd py-hack'
            sh 'ls -al'
        
        // A sleep to make sure we actually get a real difference!
        stage "Sleeping"
            sleep 10

        // And a final echo to show the time when we wrap up.
        stage "Second echo"
            echo "Wonder what time it is now?"
    }
}