import React from "react";
import ReactDOM from "react-dom";
import BatchReport from "./Report/BatchReport";
import InteractiveReport from "./Report/InteractiveReport";
import EmptyReport from "./Report/EmptyReport";

// import registerServiceWorker from './registerServiceWorker';
import "./index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from "react-router-dom";

/**
 * This single App provides multiple functions controlled via the URL path
 * accessed. We are using React-Router to control which type of report is
 * rendered and to extract the report UID from the URL when necessary.
 */
const AppRouter = () => (
  <Router>
    <Switch>
      <Route path="/testplan/:uid/:selection*" component={BatchReport} />
      <Route
        path="/interactive/:uid?/:selection*"
        component={InteractiveReport}
      />
      <Route component={EmptyReport} />
    </Switch>
  </Router>
);

ReactDOM.render(<AppRouter />, document.getElementById("root"));
// registerServiceWorker();
