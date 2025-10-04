import { View, Text, SafeAreaView } from 'react-native';
import { styles } from '../styles';

export default function Profile() {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.emptyContainer}>
        <Text style={styles.headerText}>User Profile</Text>
        <Text style={styles.emptyText}>Profile information will go here</Text>
      </View>
    </SafeAreaView>
  );
}
