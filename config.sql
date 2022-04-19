BEGIN;

DELETE FROM challenges;
INSERT INTO challenges (cid, team, t_start, t_stop) VALUES
  -- OUR CHALLANGES:
  ('Welcome(Gratulerer med gjenåpningen (for 2 måneder siden))', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('WasmWebServer', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Word', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('KnightsAndKnaves', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Base64', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('DecryptionMachine', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('CodeOfLife', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Spectogram', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Chess', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Injection', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Tree', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Platform_9_3_4', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00')),
  ('Metasyntactic', 0, datetime('now'), datetime('2022-04-22 23:15:00+02:00'));

DELETE FROM flags;
INSERT INTO flags (fid, cid, max_submissions) VALUES
  ('__zaim__{gra7u13rEr_m3D_GJENåpn1ng}', 'Welcome(Gratulerer med gjenåpningen (for 2 måneder siden))', 999999),
  ('__zaim__{k0k_i5_10v3_k0k_15_1if3}', 'Word', 999999)
;

DELETE FROM users;
DELETE FROM teams;
DELETE FROM events;
DELETE FROM submissions;
-- COMMIT;
-- DELETE ALL BELOW

INSERT INTO users (uid, password) VALUES
  -- Username: user1
  -- Password: test
  ('user1', '$argon2i$v=19$m=512,t=2,p=2$xDeorlDXJFgubKyG+YJvHQ$MC1qibUX5Ah04ZFHVPsqNQ')
;


INSERT INTO teams (tid, uid) VALUES
  ('user1', 'user1')
;



COMMIT;
