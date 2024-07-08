CREATE TABLE IF NOT EXISTS "managers" (
  "GestorID" INTEGER NOT NULL,
  "OficinaID" INTEGER,
  PRIMARY KEY ("GestorID")
);


CREATE TABLE IF NOT EXISTS "credits" (
  "CreditoID" INTEGER NOT NULL,
  "Ciclo" INTEGER,
  "MontoPendiente" REAL,
  "GestorID" INTEGER,
  PRIMARY KEY ("CreditoID"),
  FOREIGN KEY ("GestorID") REFERENCES "managers" ("GestorID") ON DELETE NO ACTION ON UPDATE NO ACTION
);


CREATE TABLE IF NOT EXISTS "offices" (
  "OficinaID" INTEGER NOT NULL,
  "Oficina" TEXT,
  PRIMARY KEY ("OficinaID"),
  FOREIGN KEY ("OficinaID") REFERENCES "managers" ("OficinaID") ON DELETE NO ACTION ON UPDATE NO ACTION
);