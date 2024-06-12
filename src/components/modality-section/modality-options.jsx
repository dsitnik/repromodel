import "./modality-options.css";

const ModalityOptions = ({ content, cardOptions }) => {
  return (
    <div className="card-deck card-break">
      {cardOptions?.map((card, idx) => (
        <div className="card" key={idx} onClick={() => setClicked(true)}>
          <div className="row">
            <div className="card-image-container">
              <div
                className="card-image"
                style={{ backgroundImage: "url('" + card.image + "')" }}
              />
            </div>

            <div className="card-title">
              <p>{card.label}</p>
            </div>
          </div>

          <div className="card-body">
            <div className="card-subtitle"> {card.numPapers}</div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ModalityOptions;
