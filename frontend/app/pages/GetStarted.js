import React from 'react';
import { ImageBackground, StyleSheet, View, Text, Image } from 'react-native';

function GetStarted({navigation}) {
    return (
        <ImageBackground 
        style= {styles.background}
        source={require('../assets/start_background.png')}>
            <Image style = {styles.imageStyle} source = {require("../assets/imgs/startLogo.png")}/>
            <View style={styles.startButton}>
            <Text style={styles.textStyle} onPress={() => navigation.navigate("Events")}>Get Started</Text>
            </View>
        </ImageBackground>
    );
}

const styles = StyleSheet.create({
    background: {
        flex:1,
    },
    startButton: {
        width: '50%',
        height: '7%',
        alignSelf: 'center',
        backgroundColor: '#3435fa',
        borderRadius: 50,
        marginTop: "130%",
        justifyContent: 'center',
        position: 'absolute',
    },
    textStyle:{
        fontFamily: 'Comfortaa',
        alignSelf: 'center',
        color: "white",
        fontSize: 20,
    },
    imageStyle: {
        position: 'relative',
        alignSelf: 'center',
        top: -75,
        borderRadius: 10,
        transform: [{
            scale: .32,
        }],
    }
})

export default GetStarted;