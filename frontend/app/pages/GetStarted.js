import React from 'react';
import { ImageBackground, StyleSheet, View } from 'react-native';

function GetStarted(props) {
    return (
        <ImageBackground 
        style= {styles.background}
        source={require('../assets/splash-icon.png')}>
            <View style={styles.startButton}></View>
        </ImageBackground>
    );
}

const styles = StyleSheet.create({
    background: {
        flex:1,
    },
    startButton: {
        width: 100,
        height: 20,
    },
})

export default GetStarted;