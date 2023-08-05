import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {css, StyleSheet} from 'aphrodite';

import DescriptionPane from './DescriptionPane';
import AssertionGroup from "./AssertionGroup";
import LogGroup from './LogGroup';
import { AssertionContext } from "../Common/context";


/**
 * Render the assertions of the selected test case.
 */
class AssertionPane extends Component {
  // Context of assertion status
  static contextType = AssertionContext;

  constructor(props) {
    super(props);

    this.state = {
      testcaseUid: undefined,
    };
  }

  /**
   * Set the state on props change. This is needed to recognize that a different
   * test case is being rendered. The state of the expand all/collapse all
   * variable is also reset.
   *
   * @param {object} props - Current props.
   * @param {object} state - Previous state.
   * @returns {object|null} - Return the new state if the test case changed or
   * null otherwise.
   * @public
   */
  static getDerivedStateFromProps(props, state) {
    if (
      props.testcaseUid === undefined
      || props.testcaseUid !== state.testcaseUid
    ) {
      return {testcaseUid: props.testcaseUid, globalIsOpen: undefined};
    }
    return null;
  }

  render() {
    let assertionPaneStyle = {
      position: 'absolute',
      left: this.props.left,
      paddingLeft: '20px',
      top: '5.5em',
      height: `calc(100% - 5.5em)`,
      width: `calc(100% - ${this.props.left})`,
    };

    if (
      this.props.assertions.length !== 0 || this.props.logs.length !== 0
      || this.props.descriptionEntries.length !== 0
    ) {
      return (
        <div style={assertionPaneStyle}>
          <div className={css(styles.infiniteScrollDiv)}>
                <DescriptionPane
                  descriptionEntries={this.props.descriptionEntries}
                />
                <AssertionGroup
                  entries={this.props.assertions}
                  filter={this.props.filter}
                  displayPath={this.props.displayPath}
                  assertionGroupUid={this.props.testcaseUid}
                  reportUid={this.props.reportUid}
                />
                <LogGroup
                  logs={this.props.logs}
                />
              </div>
        </div>);
    } else {
      return null;
    }
  }
}

AssertionPane.propTypes = {
  /** List of assertions to be rendered */
  assertions: PropTypes.arrayOf(PropTypes.object),
  /** List of error log to be rendered */
  logs: PropTypes.arrayOf(PropTypes.object),
  /** Unique identifier of the test case */
  testcaseUid: PropTypes.string,
  /** Left positional value */
  left: PropTypes.string,
  /** Assertion filter */
  filter: PropTypes.string,
  /** Report UID */
  reportUid: PropTypes.string,
  /** Selected entries' description list to be displayed */
  descriptionEntries: PropTypes.arrayOf(PropTypes.string),
};

const styles = StyleSheet.create({
  icon: {
    margin: '0rem .75rem 0rem 0rem',
    cursor: 'pointer',
  },

  infiniteScrollDiv: {
    height: 'calc(100% - 1.5em)',
    overflow: "scroll",
    paddingRight: '4rem',
    "::-webkit-scrollbar": {
      width: "6px",
    },
    "::-webkit-scrollbar-thumb": {
      backgroundColor: "rgba(0, 0, 0, 0.2)",
      borderRadius: "3px",
    },
    "::-webkit-scrollbar-thumb:hover": {
      backgroundColor: "rgba(0, 0, 0, 0.4)",
    }
  },

  buttonsDiv: {
    position: 'absolute',
    top: '0em',
    width: '100%',
    textAlign: 'right',
  },
});

export default AssertionPane;
