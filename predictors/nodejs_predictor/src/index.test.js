import nodejsPredictor from './index';

describe('index.js', () => {
  it('should say something', () => {
    expect(nodejsPredictor('🐰')).toEqual('👉 🐰 👈');
    expect(nodejsPredictor()).toEqual('No args passed!');
  });
});
