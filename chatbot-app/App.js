import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Home from './screens/Home';
import Chat from './screens/Chat';
import Profile from './screens/Profile';

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator
        initialRouteName="Home"
        screenOptions={{
          headerStyle: {
            backgroundColor: '#3b82f6',
          },
          headerTintColor: '#f8fafc',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
          drawerStyle: {
            backgroundColor: '#f8fafc',
          },
          drawerActiveTintColor: '#3b82f6',
          drawerInactiveTintColor: '#64748b',
        }}
      >
        <Drawer.Screen
          name="Home"
          component={Home}
          options={{ title: 'Home' }}
        />
        <Drawer.Screen
          name="Chat"
          component={Chat}
          options={{ title: 'AI Chat' }}
        />
        <Drawer.Screen
          name="Profile"
          component={Profile}
          options={{ title: 'Profile' }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}
