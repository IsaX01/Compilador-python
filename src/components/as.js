import React, { useState } from "react";

const SyntaxAnalyzer = () => {
  const [code, setCode] = useState("");
  const [result, setResult] = useState("");

  const handleChange = (event) => {
    setCode(event.target.value);
  };

  const handleAnalyze = () => {
    // Aquí iría la lógica de su analizador sintáctico LL
    setResult("Resultado del análisis sintáctico");
  };

  return (
    <div>
      <textarea onChange={handleChange} value={code} />
      <button onClick={handleAnalyze}>Analizar código</button>
      <textarea value={result} readOnly />
    </div>
  );
};

export default SyntaxAnalyzer;
