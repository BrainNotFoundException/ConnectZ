import React from 'react'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import { NavigationContainer } from '@react-navigation/native'
import GetStarted from './app/pages/GetStarted'
import EventsPage from './app/pages/EventsPage'

const Stack = createNativeStackNavigator()

export default function App(){
  console.log("Starting up")
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Start">
      <Stack.Screen name = "Start" component={GetStarted} options={{headerShown: false}} />
      <Stack.Screen name = 'Events' component={EventsPage} options={{headerShown: false}}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
}
