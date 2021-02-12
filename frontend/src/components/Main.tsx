import React from 'react';
import { Route, Switch } from 'react-router-dom';

import { Observer, observer } from "mobx-react";
import { Home } from '../pages/Home';
import { RootStore } from "../index";
import { MedusaMCQ } from "../pages/MedusaMCQ";
import { About } from "../pages/About";
import { Members } from "../pages/Members";
import { User } from "../pages/User";

export const Main = observer(({ store }: { store: RootStore }) => {
  return <Observer>{() =>
    <Switch> {/* The Switch decides which component to show based on the current URL.*/}
      <Route exact path='/' render={() => <Observer>{() => <Home store={store}/>}</Observer>}/>
      <Route exact path='/about' render={() => <Observer>{() => <About store={store}/>}</Observer>}/>
      <Route exact path='/members' render={() => <Observer>{() => <Members store={store}/>}</Observer>}/>
      <Route exact path='/user' render={() => <Observer>{() => <User store={store}/>}</Observer>}/>
      <Route exact path='/medusa_mcq' render={() => <Observer>{() => <MedusaMCQ store={store}/>}</Observer>}/>

    </Switch>
  }</Observer>

})
