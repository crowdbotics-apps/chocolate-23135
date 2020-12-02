import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen2181170Navigator from '../features/BlankScreen2181170/navigator';
import NotificationList2181169Navigator from '../features/NotificationList2181169/navigator';
import SignIn21181168Navigator from '../features/SignIn21181168/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen2181170: { screen: BlankScreen2181170Navigator },
NotificationList2181169: { screen: NotificationList2181169Navigator },
SignIn21181168: { screen: SignIn21181168Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
