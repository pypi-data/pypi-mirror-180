/**
 * Components to render attached files in the UI.
 */
import React from "react";
import { css, StyleSheet } from "aphrodite";

import {
  createTheme,
  ThemeProvider,
  Card,
  CardContent,
  Box,
} from "@material-ui/core";

import TextAttachment from "./TextAttachment";
import AttachmentAssertionCardHeader from "./AttachmentAssertionCardHeader";
import { getAttachmentUrl } from "../../Common/utils";

// TODO: move theme out to a common place
const theme = createTheme({
  typography: {
    fontFamily: [
      "-apple-system",
      "BlinkMacSystemFont",
      "Segoe UI",
      "Roboto",
      "Helvetica Neue",
      "Arial",
      "Noto Sans",
      "sans-serif",
      "Apple Color Emoji",
      "Segoe UI Emoji",
      "Segoe UI Symbol",
      "Noto Color Emoji",
    ].join(","),
  },
});

/**
 * Generic file attachments component.
 *
 * Provides both a direct link to download the file and optionally a rendered
 * preview of the file for supported filetypes. Currently images and text
 * files can be previewed.
 */
export const AttachmentAssertion = (props) => {
  const content = getAttachmentContent(props.assertion, props.reportUid);
  return <ThemeProvider theme={theme}>{content}</ThemeProvider>;
};

/* Render the attachment content, depending on the filetype. */
const getAttachmentContent = (assertion, reportUid) => {
  const fileType = assertion.orig_filename.split(".").pop();
  const filePath = assertion.dst_path;
  const description = assertion.description;
  const getPath = getAttachmentUrl(filePath, reportUid, null);

  switch (fileType) {
    case "txt":
    case "log":
    case "out":
    case "csv":
    case "stdout":
    case "stderr":
      return (
        <TextAttachment
          src={getPath}
          file_name={assertion.orig_filename}
          file_size={assertion.filesize}
          devMode={reportUid === "_dev"}
        />
      );

    case "jpeg":
    case "jpg":
    case "bmp":
    case "png":
      return (
        <Card>
          <AttachmentAssertionCardHeader
            src={getPath}
            file_name={assertion.orig_filename}
            file_size={assertion.filesize}
          />
          <CardContent>
            <Box mx="auto" width="fit-content">
              <figure>
                <img src={getPath} alt={description} />
                <figcaption className={css(styles.caption)}>
                  {description}
                </figcaption>
              </figure>
            </Box>
          </CardContent>
        </Card>
      );
    default:
      // When running the development server, the real Testplan back-end is not
      // running so we can't GET the attachment. Stick in a button that
      // gives a debug message instead of the real link.
      return (
        <Card>
          <AttachmentAssertionCardHeader
            src={getPath}
            file_name={assertion.orig_filename}
            file_size={assertion.filesize}
          />
        </Card>
      );
  }
};

const styles = StyleSheet.create({
  caption: {
    "text-align": "center",
  },
  contentSpan: {
    lineHeight: "110%",
  },
});

export default AttachmentAssertion;