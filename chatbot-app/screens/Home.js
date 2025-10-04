import { View, Text } from 'react-native';
import { styles } from '../styles';

export default function Home() {
  return (
    <View style={styles.container}>
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyText}>Welcome to AI Chatbot</Text>
      </View>
    </View>
  );
}
