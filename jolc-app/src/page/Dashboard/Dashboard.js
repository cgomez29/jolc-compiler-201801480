import React, { useContext, useState } from "react";
import "react-toastify/dist/ReactToastify.css";
import "codemirror/mode/julia/julia";
import "codemirror/mode/go/go";
import "codemirror/theme/dracula.css";
import "codemirror/theme/blackboard.css";
import "codemirror/addon/edit/matchbrackets";
import "codemirror/lib/codemirror.css";
import url from "../../config";

import { UnControlled as CodeMirror } from "react-codemirror2";
import { UserContext } from "../../context/UserContext";

import axios from "axios";
import "./setup-codemirror.css";
import Table from "../../components/Table/Table";
import { ToastContainer, toast } from "react-toastify";

export const Dashboard = () => {
  const { inputText, setInputText } = useContext(UserContext);
  const { outputText, setOutputText } = useContext(UserContext);
  const { setDot, setErr, err, setSymbols } = useContext(UserContext);

  const [code] = useState(inputText);

  const notifySuccessful = () => toast("Successful!");
  const notifyError = () => toast("Error!");

  const execute = async () => {
    await axios
      .post(`${url}/compile`, { input: inputText })
      .then((res) => {
        if (res.data.err !== "[]") {
          notifyError();
          setErr(res.data.err);
          // setOutputText('');
        } else {
          notifySuccessful();
          setErr("");
        }
        setOutputText(res.data.result);
        setDot(res.data.dot);
        setSymbols(res.data.symbol);
      })
      .catch((err) => {});
  };

  const headers = {
    head1: "Index",
    head2: "Description",
    head3: "Row",
    head4: "Column",
    head5: "Date and Time",
  };

  return (
    <>
      <div className="container-xl">
        <div className="row">
          <div className="col-s">
            <button type="button" onClick={execute} className="btn btn-dark">
              Execute
            </button>
            <button type="button" onClick={execute} className="btn btn-dark">
              Mirilla
            </button>
            <button type="button" onClick={execute} className="btn btn-dark">
              Bloque
            </button>
            <button
              type="button"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              className="btn btn-light"
            >
              Errors
            </button>
          </div>
          <div className="col-md-6">
            <CodeMirror
              value={code}
              options={{
                lineNumbers: true,
                mode: "julia",
                theme: "dracula",
              }}
              onChange={(editor, data, value) => {
                setInputText(editor.getValue());
              }}
            />
          </div>
          <div className="col-md-6">
            <CodeMirror
              value={outputText}
              options={{
                lineNumbers: true,
                mode: "go",
                theme: "blackboard",
                readOnly: true,
              }}
              onChange={(editor, data, value) => {
                setOutputText(value);
              }}
            />
          </div>
        </div>
      </div>
      <div className="modal" id="exampleModal">
        <div className="modal-dialog modal-lg" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title">Errors</h5>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true"></span>
              </button>
            </div>
            <div className="container">
              <div className="row">
                <div className="col-md-12">
                  <Table headers={headers} data={err} />
                </div>
              </div>
            </div>
            <div className="modal-footer"></div>
          </div>
        </div>
      </div>
      <ToastContainer
        position="top-center"
        autoClose={1800}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
    </>
  );
};
