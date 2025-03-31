import React from 'react';
import { ImageBackground, StyleSheet, View, Text } from 'react-native';
import { useFonts } from 'expo-font';

function GetStarted(props) {
    return (
        <ImageBackground 
        style= {styles.background}
        source={require('../assets/start_background.png')}>
            <View style={styles.startButton}>
                <Text style={styles.textStyle}>Get Started</Text>
            </View>
        </ImageBackground>
    );
}

const styles = StyleSheet.create({
    background: {
        flex:1,
    },
    startButton: {
        width: '60%',
        height: '7%',
        alignSelf: 'center',
        backgroundColor: '#3435fa',
        borderRadius: 40,
        marginTop: "130%",
        justifyContent: 'center',
    },
    textStyle:{
        fontFamily: 'Comfortaa',
        alignSelf: 'center',
        color: "white",
        fontSize: 20,
    }
})

export default GetStarted;